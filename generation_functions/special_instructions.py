from itertools import product
import random

def combine_traits(personality_matrix): # GPT-generated
    # Using itertools.product to generate all possible combinations
    combinations = product(*personality_matrix)
    
    # Joining each combination into a single string
    combined_traits = ["\n".join(combination).strip().replace("\n\n","\n") for combination in combinations]
    
    return combined_traits

def special_instructions(n=1,non_axis_traits=False,non_axis_traits_only=False):
    """
    documentation todo
    """
    
    ### NOTE on how traits are planned out for this step ###
    # Here's the copy-pasted rambling thoughts from my planning document. 
    # CHARACTER PLANNING
    # Consider that we can represent a character's personality might lie as a vector with multiple dimensions. Now, we could define any number of individual dimensions, and lots of them would be right: intelligence, extraversion, industriousness, etc. But in the default version of the Augmentool we're doing roleplay, so we want to pick a set of dimensions using which we can describe accurately and concisely the characters that might show up in a roleplay. Consider that if a personality trait is a vector in 3-space, we want to pick traits that aren't coplanar -- ie, that describe something unique. Ideally, they'd all be perpendicular -- maximally unique traits.
    # I belive I have found 3 such axes that are useful for roleplay:
    # Assertiveness
    # Kindness/Morality
    # Horniness (one of the few things we have an edge over GPT in)
    # So we have
    # Chaste------------------------------------normal----------------------------------------------------------------Slaanesh
    # Shy/Withdrawn/Timid (Bocchi)--------------Has moments of shyness and courage------------------------------------James Bond
    # Kind--------------------------------------Often good, capable of bad — and can be convinced to do it -----------politician
    # We make more verbose descriptions of each trait and place them in a matrix, reflecting the visualization above. We then create a list of all possible combinations of one item from each row and randomly sample from it for the special instruction.
    
    # Two additional dimensions I added afterwards: intellectual sophistication, and age. I might add these if testing shows that the AI can handle them, but no few-shot example has anywhere near 5 combinations, so we'll see.
    
    ## NOTE You may (and are encouraged to!) add your own trait dimensions here, to make the character personalities used more accurately reflect your specific usecase and preference. Since every possible combination of one trait from each row is put into the list, you will get a lot of variety with your characters for not much work.
    # NOTE Chaste and puritan characters have a tendency to be interpreted by the AI as being religious, possibly because of "puritan" even though I initially just meant for this to be the opposite of horny.
    
    axis_traits = [
            [
                "The character should be chaste and puritanical.",
                "", 
                "The character should be very seductive and flirtatious."
            ], # Horniness (middle deliberately left blank so that the model does not mention it)
            [
                "The character should be shy, withdrawn, and timid.", 
                "The character should be neither particularly bold, nor particularly timid.", 
                "The character should be assertive and bold."
            ], # Assertiveness
            [
                "The character should be kind and agreeable.", 
                "The character should have both good and bad sides.", 
                "The character should be an awful person, and should be enjoying every second of it."
                # "The character should be an awful person, possessing a number of vices (that are compatible with the previously-mentioned instructions)."
            ], # Kindness/Morality
            # ["The character should be a young adult.", "the character should be middle-aged." "The character should be in late adulthood."], # Age group
            # ["The character should be unsophisticated and crude.", "The character should be decently smart and refined.", "The character should be the epitome of intellectual sophistication."],
        ]
    
    non_axis_trait_list = [ # The following are examples of traits that are not on the axes above, but are still useful for character creation. I've not tested all of them, and I've not tested them in combination with the axis traits. But if you prefer a more manual approach to character creation, you can use stuff like this.
        """The character should be a Japanese High School student.
The character should be a girl.
The character should be decently smart, but not genius-level.
The character should be very kind, but too gentle and too much of a pushover for their own good.""",
        """The character should be an awful person, and enjoying every second of it.
The character should be intellectually brilliant.
The character should be condescending and rude.""",
"""The character should be a young adult.
The character should be antisocial and coarse.
The character should be a smoker."""
"""The character should be middle-aged.
The character should be"""
        # """The character should be a catgirl who inserts "nya" into every sentence. and makes cat puns.""", # someone actually has to do this, I'm serious, it'll be purrfect, nya~
        # """The character should be edgy and nihilistic."""
            ]
    
    if not non_axis_traits_only:
        traits = combine_traits(axis_traits)

        selected_traits = random.sample(traits, 1)
        if non_axis_traits:
            
            selected_traits += random.sample(non_axis_trait_list,1)
        
    if non_axis_traits_only:
        selected_traits = random.sample(non_axis_trait_list,1)

    # Return the combined string, with each sentence on a new line
    return selected_traits[0]