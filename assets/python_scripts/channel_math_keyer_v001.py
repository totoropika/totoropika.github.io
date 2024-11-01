n = nuke.thisNode()
k = nuke.thisKnob()



if k.name() in ("first_channel", "second_channel", "third_channel"): # Only affect channel knobs

    # Define the channel mappings
    red_mapping = [(0, 'rgba.red', 'rgba.red'), (0, 'rgba.red', 'rgba.green'), (0, 'rgba.red', 'rgba.blue'), (0, 'rgba.red', 'rgba.alpha')]
        
    green_mapping = [(0, 'rgba.green', 'rgba.red'), (0, 'rgba.green', 'rgba.green'), (0, 'rgba.green', 'rgba.blue'), (0, 'rgba.green', 'rgba.alpha')]
        
    blue_mapping = [(0, 'rgba.blue', 'rgba.red'), (0, 'rgba.blue', 'rgba.green'), (0, 'rgba.blue', 'rgba.blue'), (0, 'rgba.blue', 'rgba.alpha')]
        
    no_mapping = [(-1, 'black', 'rgba.red'), (-1, 'black', 'rgba.green'), (-1, 'black', 'rgba.blue'), (-1, 'black', 'rgba.alpha')]

    enable = True
    disable = False
    # Assign corresponding shuffle node to channel knob
    with n:
        if k.name() == "first_channel":
            shuffle = nuke.toNode("Shuffle1")
            merge = nuke.toNode("Merge1")
            grade = nuke.toNode("Grade1")
            toggle = nuke.toNode('Switch1')
        elif k.name() == "second_channel":
            shuffle = nuke.toNode("Shuffle2")
            merge = nuke.toNode("Merge1")
            grade = nuke.toNode("Grade2")
        elif k.name() == "third_channel":
            shuffle = nuke.toNode("Shuffle3")
            merge = nuke.toNode("Merge2")
            grade = nuke.toNode("Grade3")
        shuffle_mappings = shuffle.knob('mappings')
        #merge_operation = merge.knob('operation')
        #grade_blackpoint = grade.knob('blackpoint')
        #grade_whitepoint = grade.knob('whitepoint')

            
        
    # Set value of shuffle according to channel knob value
    with n:   
        if k.value() == 'red':
            shuffle_mappings.setValue(red_mapping)
        elif k.value() == 'green':
            shuffle_mappings.setValue(green_mapping)
        elif k.value() == 'blue':
            shuffle_mappings.setValue(blue_mapping)
        elif k.value() == 'none':
            shuffle_mappings.setValue(no_mapping)
                
        else:
            print("Error occurred")

    with n:
        if k.name() == "first_channel":
            if k.value() == "none":
                toggle.knob('which').setValue(1.0)
            else:
                toggle.knob('which').setValue(0)
        else:
            pass

    with n:
        if k.value() == 'none':
            merge.knob('disable').setValue(True)
            grade.knob('disable').setValue(True)
        else:
            merge.knob('disable').setValue(False)
            grade.knob('disable').setValue(False)
