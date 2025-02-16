##### **Objective:**

Become a **PyCharm Power User** by completing a set of **mini-challenges** that reinforce key IDE features. Each task requires using **PyCharm-specific tools** instead of manually coding everything.

#### **📜 Instructions**

1. Use the starter Python script (provided below).
2. Make a specific folder in your individual GIT repo for this (and all other assignments).
3. Follow the steps to fix, improve, and analyze the code using PyCharm’s features.
4. Commit changes every 1-3 steps with meaningful commit messages.
5. Submit a link to the folder with your final, well-formatted, and optimized script.

#### **🐍 Starter Code (Intentionally Messy!)**

Students will be provided with the following buggy, inefficient, and unoptimized script:

```python
def p(b):
 for r in b:
  print(" | ".join(r))
  print("-"*5)

def c_w(b,p):
 for i in range(3):
  if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
   return True
 if all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3)):
  return True
 return False

def f(b):
 return all(c!=" " for r in b for c in r)

def t():
 b=[[" "for _ in range(3)]for _ in range(3)]
 p=["X","O"]
 print("Tic-Tac-Toe Game")
 p(b)
 for t in range(9):
  pl=p[t%2]
  while 1:
   try:
    r,c=map(int,input(f"P {pl}, row col (0-2): ").split())
    if b[r][c]==" ":
     b[r][c]=pl
     break
    else:
     print("Nope. Again.")
   except:
    print("Wrong. 0-2 pls.")
  p(b)
  if c_w(b,pl):
   print(f"P {pl} wins!")
   return
  if f(b):
   print("Draw!")
   return
 print("Draw!")

t() 
```

#### **🔍 Task List (Each Task Uses a Key PyCharm Feature)**

❌ **Rename stuff and make it better** → Use **Refactor > Rename** (Shift + F6)<br>
❌ **Reformat the code using auto-formatting** → Use **Code > Reformat Code** (Ctrl + Alt + L)<br>
❌ **Run Code Analysis & Fix Warnings** → Use **Inspect Code** (Code > Inspect Code)<br>
❌ **Extract some code from t() and make it cleaner**→ Use **Refactor > Extract Method**(Ctrl + Alt + M)<br>
❌ **Add a breakpoint & step through execution** → Use **Debugging Tools** (Ctrl + F8)<br>
❌ **Create a docstring for each function** → Use **PyCharm's Generate Docstring** (Alt + Enter) or Use **AI** (Ctrl + \)<br>
❌ **Run the script with Code Coverage enabled** (Run > Run with Coverage)<br>
❌ **Use Git to track changes & commit the final version** (Ctrl + K to commit)<br>