import os
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style("ticks")


def get_connection_to_db():
    USERNAME = "russian_economy_db_owner"
    PASSWORD = os.environ['pass']
    HOST = "ep-restless-dust-a2uu19hg.eu-central-1.aws.neon.tech"
    DATABASE = "russian_economy_db"
    conn_str = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?sslmode=require'
    engine = create_engine(conn_str)
    return engine

def get_main_data_from_db(engine):
    query = "SELECT * FROM russian_economy"
    data = pd.read_sql(query, engine)

    data['construction_real'] = data['construction'] / (1 + data['annual_inflation'] / 100)
    data['education_real'] = data['education'] / (1 + data['annual_inflation'] / 100)
    data['healthcare_and_social_services_real'] = data['healthcare_and_social_services']  / (1 + data['annual_inflation'] / 100)

    prev_year = data[['construction_real', 'education_real', 'healthcare_and_social_services_real']].shift(1).rename(columns={
    'construction_real': 'construction_real_prev', 
    'education_real': 'education_real_prev', 
    'healthcare_and_social_services_real': 'healthcare_and_social_services_real_prev'
    })

    data = pd.concat([data, prev_year], axis=1)
    data['construction_growth'] = (data['construction_real'] / data['construction_real_prev'] - 1) * 100
    data['education_growth'] = (data['education_real'] / data['education_real_prev'] - 1) * 100
    data['healthcare_and_social_services_growth'] = (data['healthcare_and_social_services_real'] / data['healthcare_and_social_services_real_prev'] - 1) * 100

    return data

def create_plot_1(data):
    fig, ax = plt.subplots()
    
    plt.plot(data['year'], data['construction'], 'g', label='Строительство')
    plt.plot(data['year'], data['education'],'r',label='Образование')
    plt.plot(data['year'], data['healthcare_and_social_services'], 'b', label='Здравоохранение и оказание социальных услуг')
    plt.legend(loc='best')
    plt.box(False)
    
    return fig, ax

def create_plot_2(data):
    fig, ax = plt.subplots()
    
    plt.plot(data['year'], data['construction'], '--', label='Номинальные заработные платы')
    plt.plot(data['year'], data['construction_real'], label='Реальные заработные платы')
    plt.legend(loc='best')
    plt.box(False)
    
    return fig, ax

def create_plot_3(data):
    fig, ax = plt.subplots()
    
    plt.plot(data['year'], data['education'],'--',label='Номинальные заработные платы')
    plt.plot(data['year'], data['education_real'], label='Реальные заработные платы')
    plt.legend(loc='best')
    plt.box(False)
    
    return fig, ax

def create_plot_4(data):
    fig, ax = plt.subplots()
    
    plt.plot(data['year'], data['healthcare_and_social_services'], '--', label='Номинальные заработные платы')
    plt.plot(data['year'], data['healthcare_and_social_services_real'], label='Реальные заработные платы')
    plt.legend(loc='best')   
    plt.box(False)
    
    return fig, ax 
       
def create_plot_5(data):
    fig, ax = plt.subplots()
    
    plt.plot(data['year'], data['construction_growth'], label='Строительство', alpha=0.5)
    plt.plot(data['year'], data['education_growth'],label='Образование', alpha=0.5)
    plt.plot(data['year'], data['healthcare_and_social_services_growth'], label='Здравоохранение и оказание социальных услуг', alpha=0.5)
    plt.plot(data['year'], data['annual_inflation'], label='Годовая инфляция')
    plt.legend(loc='best')
    plt.box(False)

    return fig, ax 
    