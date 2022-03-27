getting_started = """
Getting Started with Java in VS Code
This tutorial shows you how to write and run Hello World program in Java with Visual Studio Code. It also covers a few advanced features, which you can explore by reading other documents in this section.

For an overview of the features available for Java in VS Code, see Java Language Overview.

If you run into any issues when following this tutorial, you can contact us by entering an issue.

Setting up VS Code for Java development#
Coding Pack for Java#
To help you set up quickly, you can install the Coding Pack for Java, which includes VS Code, the Java Development Kit (JDK), and essential Java extensions. The Coding Pack can be used as a clean installation, or to update or repair an existing development environment.
"""

with open("getting_started.txt", "wt") as fout:
    size = len(getting_started)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        fout.write(getting_started[offset:offset+chunk])
        offset += chunk
