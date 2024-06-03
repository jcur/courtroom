# ==========================
#  Case specific procedure
# ==========================

def get_procedure():

    '''
    Returns a dictionary of instructions with key facts on the shoplifting case.
    '''

    regular_procedure = {

    'claim_prosecutor': f''' 
    Here is the exact claim:
    Madam x is accused of shop lifting on March 12, 2024, she was 
    seen in video camera which the prosecution will produce, stealing
    7 pairs of earings at 3:14pm in the afternoon, which she put in her pockets. 
    At 3:15pm, she is seen by another camera leaving the store.
     ''',

    'plea_defendant': f''' 
    If user asks a specific question to defendant, then defendant answers the exact question concisely, based on defendant's knowledge on the events. 
    When defendant answers a question, she only provide information relevant to the question, nothing more.
    Here is the exact plea:
    In short, I did put the earings in my pocket but only because I wanted to buy 
    them and got a phone call at the same moment. After I picked up the phone,
    my friend on the phone told me she needed to speak to me and was crying, so
    I forgot about the hearings on the moments and left as I was talking to my friend.
    I only realized once I was home that I had the earings in my pocket. 
    I wanted to bring them back but I was worry no one would trust me.
     ''',

    'version_of_events_prosecutor': f''' 
    Here is the exact version of events: 
    As you can see on the videos, she is checking that no one is looking at her seconds
    before she inserts the earrings in her pocket. Even though the angle of the camera 
    can't clearly conclude, she doesn't seem to be picking up her phone at that moment.
     ''',

    'version_of_events_defendant': f''' 
    Here is the exact version of events:
    As you can see on the second video, my client is cleary talking on the phone as she 
    leaves the store, corroborating my client's claim that she got distracted by her friend
    crying on the phone.
     ''',

    'witness': f'''
    If user does not ask a question to witness, then witness just says hello.
    If user asks a question to witness, then witness answers the exact question concisely, based on witness's knowledge on the events. 
    When witness answers a question, she only provide information relevant to the question, nothing more.
    Here is the exact witness's knowledge on the events:
    Witness is a cashier at the store. 
    Witness name is Julia, and is 29 years old.
    Witness remembers the defendant being in the store on March 12, 2024.
    Witness remembers the defendant walking very fast toward the exit.
    Witness does not remember if the defendant was talking on the phone.
     ''',

    'background_defendant': f'''
    Here is the exact background of the defendant:
    I will make it short, I have never stole anything in my life.
     ''',

    'income_and_family_defendant': f'''
    Here is its exact income and family situation of the defendant:
    I have two kids, and win $47,000 per year, I'm a high-school teacher.
     ''',

    'closing_statement_prosecutor': f''' 
    Here is the closing statement of the prosecutor: 
    The prosecution has no doubt on this matter, Madam x was seen on multiple cameras, 
    stealing multiple pairs of earrings, and the witness confirmed a very abnormal behavior 
    from the defendant on that day. She stole those earrings. Prosecution rests.
     ''',

    'closing_statement_defendant': f''' 
    Here is the closing statement of the defendant:  
    It is true the defendant was seen on leaving the store, 
    and even putting the earrings in her pocket. 
    But context matters. She got a phone call. She got disturbed.
    She got emotional with her friend and didn't want to make a scene in the store.
    She was absorbed by her friend's cry for help. 
    In short: she forgot. Aren't we all forgetting things from time to time?
    Forgetting something is not a criminal act. That is the defendant is innocent.
     '''

    # 'communication_of_verdict_date': f'''
    # If the user communicates a verdict date, end the game
    # '''

    }

    return regular_procedure
