# Contributed by: Team 3
def menuFeature():
    """Reprints the menu."""
    
    menu_titles = ["Student Transcript Generation System", "="*56, "1. Student details", 
    "2. Statistics", "3. Transcript based on major courses", "4. Transcript based on minor courses", "5. Full Transcript", 
    "6. Previous Transcript Requests", "7. Select another student", "8. Terminate the system"]

    print("="*60)
    for i in menu_titles:
        if i == menu_titles[0]: # for the title
            i = i.center(60, "=")
            print(i)
            continue
        i = "{:<}".format(i)
        i = i.ljust(56, " ")
        print("=", i, "=")
    print("=" * 60)

if __name__ == '__main__':
    menuFeature()
    