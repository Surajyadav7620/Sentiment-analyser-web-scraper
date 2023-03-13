                                                            Data Extraction and NLP
                                                            
                                                            
                                                            
                          Steps to run the project
                          1.Create a new environment

                             conda create -p venv python==3.7 -y
                          2.Run requirments.txt
                          3.Load Input.xlsx file
                          4.webscraper.py 
                          Desc:1.The code reads a list of URLs from an input file called Input.xlsx.
                               2.For each URL in the input file, the code calls a function called extract_article_text() to extract the title and text of the                                    article.
                               3.If the article is not found, the code skips it and moves on to the next URL.
                               4.If the article is found, the title and text are added to a new DataFrame called output_df.
                               5.The final output_df is written to an output file called Output.xlsx.
                               6.The output file contains the URL ID, title, and text for each article that was successfully extracted.
                               7.This code can be used as a starting point for a web scraping project that involves extracting article titles and text from                                      multiple URLs and storing the results in a structured format.
                               8.This code uses the requests, beautifulsoup4, pandas, and openpyxl libraries, so these libraries need to be installed before                                      running the code.
                          
                          5.textanalyser.py 
                            After running this it provide you the Output_data_structure.xlsx which comtain sentiment analysis scores.
                          6.RUN app.py to call webscraper and textanalyser and RUN the complete project.
                                                   
                                                   
                                                                     Done
                          