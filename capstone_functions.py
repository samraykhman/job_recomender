import requests 
import pandas as pd 
import json 
import numpy as np
import pprint
from bs4 import BeautifulSoup
import time
import numpy as np
import string
import re
import unidecode

# function to retrieve link of every job posting
def get_hyperlinks(url, header):
    """
    Gets the hyperlink of every job posting on stackoverflow's job post portal
    
    Parameters:
    -----------
    url: string
        page of stackoverflow with multiple job postings
    header:
        user-agent request header in case website would not let me get data otherwise
    Returns:
    --------
    all_hyperlinks: list
        list of each hyperlink that related to a job posting on stackoverflow
    """
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    
# table holds the preview of every job posting
    job_table = soup.find_all('h2', {'mb4 fc-black-800 fs-body3'})
    
    for job in job_table:
#         retrieving every link
        job_link_html = job.find_all('a', href=True)
        
        for job_link in job_link_html:
            all_hyperlinks.append('https://stackoverflow.com'+ job_link['href'])
            
    return all_hyperlinks

# function to retreive info about each job posting
def each_job(url):
    """ 
    Gets the job's position title, technology, description, overview

    Parameters:
    -----------
    url: string
        the hyperlink of a job posting
    Returns:
    --------
    job_desc_list: dict
        dictionary of information of each job
    """
    time.sleep(2)
    
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
# code for scraping technology required
# making target variable out of this column, doing try & except so i can later drop row from df
    tech = []
    try:
        job_tech = soup.find_all('section', {'class':'mb32'})[1]('a')
        for x in job_tech:
            tech.append(x.text)
    except IndexError:
        tech = np.nan
# code for scraping overview of the posting
    overview = ''
    try:
        job_overview = soup.find_all('section', {'class':'mb32'})[2](['p', 'ul'])
        for y in job_overview:
            overview += y.text
    except IndexError:
        overview = np.nan
# code for scraping the job position
    try:
        position = [soup.find_all('h1', {'class':'fs-headline1 mb4'})[0].text]
    except IndexError:
        position = np.nan
# code for brief insight
    try:
        about = [soup.find('section', {'class':'mb32'})('div')[1].text]
    except (IndexError, TypeError):
        about = np.nan
# creating dictionary for each job posting
    job_post_dict = {
        'position':position,
        'description':about,
        'languages':tech,
        'overview':overview}
# creating list of job postings to later turn into a dataframe
    job_desc_list.append(job_post_dict)
    
    return job_desc_list

# function to clean the text that was scraped
def clean_text(text):
    """
    Make text lowercase and remove text in square brackets, punctuation, useless characters, and words with numbers in them

    Parameters:
    -----------
    text: string
        value of a certain column in a dataframe that corresponds to something from the job posting
    Returns:
    -------- 
    text:
        cleaned version of the same text
    """
    
    text = unidecode.unidecode(text)
    text.replace('\\n', '')
    text.strip(' \\n')
    text = re.sub(pattern, ' ', str(text))
    text = re.sub('(\\*n)', ' ', str(text))
    text = re.sub('\w*\d\w*', ' ', str(text))
    text = re.sub('  ', ' ', str(text))
    return text

# function for each job posting's description, get rid of stop words and uneccesary characters
def fix_description(text):
    """
    Cleans descritpion column specifically, since clean_text function did not complete the job
    
    Parameters:
    -----------
    text: string
        value of description column which is body of text
    Returns:
    --------
    final_joined: string
        cleaned description body
    """
    separate = text.split()
    joined = ' '.join(list([x.strip('\\n') for x in d]))
    final_joined = ' '.join(hell.split('\\n')[::3])
    return final_joined

# function to keep each job's position title, without uneccessary characters
def keep_position_name(text):
    """
    Cleans position_title column specifically, since clean_text function did not complete the job
    
    Parameters:
    -----------
    text: string
        value of position_title column which is body of text
    Returns:
    --------
    text: string
        cleaned job position title
    """
    text = text[3:]
    return text

# code to tokenize text manually instead of relying on sklearn's tfidf vectorizer
def tokenize(text):
    """
    Tokenizes the text data

    Parameters:
    -----------
    text: string
        value of a column that needs tokenizing
    Returns:
    --------
    text: list
        tokenized list of strings
    """
    text = [word_tokenize(x) for x in text]
    return text

