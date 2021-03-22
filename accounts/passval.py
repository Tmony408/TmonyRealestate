
def password_checker(password):
    keywords = set(password)
    lower = any(keyword.islower() for keyword in keywords)
    upper = any(keyword.isupper() for keyword in keywords)
    correct_characters =any(keyword.isnumeric() for keyword in keywords) and any(keyword.isalpha() for keyword in keywords)
    
    return lower and upper and correct_characters
