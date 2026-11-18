# CP1404 Assignment 2 - Song Supply 2.0 by YOUR_NAME

A Python project with GUI and Console programs that (re)use classes to manage a list of songs to learn.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you?

The entire project took me approximately 5 hours in total. I divided the work over a few sessions: 
- About 2 hours were spent designing the `Song` and `SongCollection` classes and writing the test cases. 
- 1 hour were spent refactoring the console program from Assignment 1 to use classes and JSON.
- The remaining 2 hours were dedicated to the Kivy GUI implementation, debugging, and refining the layout.

## 2. What are you most satisfied with?

I am most satisfied with how cleanly the `Song` and `SongCollection` classes integrate into both the console program and the Kivy GUI. By completely separating the data model from the user interface, I was able to reuse the exact same logic for loading, sorting, and updating songs in two completely different environments without rewriting the core code. I am also proud of getting the dynamic button generation and the color-coding for learned/unlearned songs to work smoothly in the GUI.

## 3. What are you least satisfied with?

I am least satisfied with how much time I spent debugging the Kivy layout and environment issues. For example, I initially struggled with the `ParserException` because my `app.kv` file had multiple root widgets. I also had a `NameError` because I forgot to define the `UNLEARNED_MARKER` constant during refactoring. These were simple mistakes that could have been avoided with better attention to detail and smaller, incremental testing.


## 4. What worked well in your development process?

The incremental Git commit strategy worked extremely well. By committing after finishing the classes and tests, then again after refactoring the console program, and finally for the GUI, I always had a working fallback point. Additionally, writing the test files (`test_song.py` and `test_songcollection.py`) first gave me confidence that my classes were robust before I started building the UI on top of them. 

## 5. What about your process could be improved the next time you do a project like this?

Next time, I will test my data files (like the JSON file) immediately after setting up the repository. I lost time at the beginning due to a `KeyError` because the starter `songs.json` was missing the `"learned"` key. I should have validated the JSON structure right away. For GUI development, I should build the interface in smaller chunks (e.g., test just the left panel, then just the right panel) rather than writing the entire `.kv` file at once.

## 6. Describe what learning resources you used and how you used them.

I primarily used the subject materials, specifically the KivyDemos provided in the lectures. The `dynamic_widgets` and `spinner_demo` examples were crucial for understanding how to dynamically generate buttons in Python and how to bind the Spinner to a sorting function. I also heavily relied on the official Kivy documentation to understand `.kv` syntax and layout properties. Finally, PyCharm's error tracebacks were my most frequent "resource" for pinpointing exact line numbers when errors occurred.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The biggest challenge was connecting the Kivy GUI to the Python logic. Specifically, I encountered a `ParserException` because I accidentally left multiple root widgets in the `app.kv` file. I overcame this by clearing the file and ensuring only one `BoxLayout` existed at the top level. Another challenge was dealing with `KeyError` when loading JSON. I resolved this by carefully inspecting the JSON file format and ensuring the keys matched exactly what `SongCollection` expected (`title`, `artist`, `year`, `learned`). Debugging these errors step-by-step helped me deeply understand the Kivy framework and Python dictionary manipulation.
