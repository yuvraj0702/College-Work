def concatenate_names(first_name="", middle_name="", surname=""):
    full_name = first_name + " " + middle_name + " " + surname
    return full_name.strip()



print("Full Name:", concatenate_names(first_name="yuvraj", middle_name="pratap", surname="Singh"))