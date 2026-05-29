prompts:

Next step run over files and call the metods:

create a code that 


-load image_description.json file from folder (if exist or create new) to dict

-load keywords with load_keywords method and set keywords dict

then run over image files by mask setted in config ("*.jpg", "*.png") in selected folder and 

-get file name 


-convert it to image_name -  remove last symbols if exist and extention for example "green robot (1).jpg" -> "green robot" , "red apple.png" -> "red apple"


-sanitise file name and get new filename (with extention)



-get keyword from keywords dict (main_keywords + optional_keywords) based on image_name as a key

-add / update field in dict image_description : new filename  as a key, { image_name, description - (string wil setup letter), description_lenght as len() of description, keywords - array, count - len of keywords)



-if no keywors found set warning in image_name



after interation end save image_description.json  file back to the folder