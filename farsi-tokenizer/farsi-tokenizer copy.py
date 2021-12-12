import subprocess, re

def farsi_verb_tokenizer(sentence):
    """

    perl ./script/farsi-verb-tokenizer.perl test-input.txt > test-output.txt
    
    """

    cmd = f"perl ./scripts/farsi-verb-tokenizer.perl '{sentence}'"

    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return output

def post_process(line):
    final_res = []
    connected_words = ["ها","هایی","هایشان","هایش","های","های","های","هایی","ام","ای","ای","اد","ایم","اید","اید","اند","اند","اند","اند","تر","ترین","ترین"," ای"]
    before_words = ["بی","نا"]
    a = " ".join(re.split('\W+',line))
    line_split = line.split(" ")
    for word in connected_words:
        if len(line_split) <= len(word) :
            continue
        if word in line_split[2:]  :
            indx = line_split[2:].index(word)+2    
            line_split[indx-1] += "_"+ word
            line_split.__delitem__(indx)
    for word in before_words:
        if len(line_split) <= len(word) :
            continue 
        if word in line_split[2:]  :
            indx = line_split[2:].index(word)  +2     
            line_split[indx+1] = "_"+ word + line_split[indx +1]
            line_split.__delitem__(indx)
    
    for word in line_split :
        word = word.replace("\n","")
        if word == " " or word == "\n" or word == "" or "\n" in word:
            continue

        made_word = word.replace('_','\u200c')
        final_res.append(made_word)
    return " ".join(final_res)

def tokenize(sentence):
    data = farsi_verb_tokenizer(sentence).decode('unicode-escape').encode('latin1').decode('utf-8').strip()
    try:
        return post_process(data)
    except:
        return data

print(tokenize("علی به آنها گفته بود."))