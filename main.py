from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'Shell> '
    intro = '''Welcome to Big Data Processing Application
Please type the number that corresponds to which application you would like to run:
1. Apache Hadoop
2. Apache Spark
3. Jupyter Notebook
4. Sonarqube And Sonarscanner 

Type the number here >'''

   
    def do_hadoop (self,inp):
        print('Click on URL below for Apache Hadoop:')
        link = "http://34.70.67.87:9870/dfshealth.html#tab-overview"
        print(link)

    def do_spark(self, inp):
        print('Click on URL below for Apache Spark:')
        link = "http://34.123.150.253:8080/"
        print(link)

    def do_jupyter(self, inp):
        print('Click on URL below for Jupyter Notebook:')
        link = "http://104.154.151.198:8888/login?next=%2Ftree%3F"
        print(link)

    def do_sonar(self, inp):
        print('Click on URL below for SonarQube:')
        link = "http://35.224.173.90:9000/sessions/new?return_to=%2F"
        print(link)

    def do_unrecognised(selfself,inp):
        print('Unrecognized input , Type a number between 1-4')

    def do_exit(self, inp):
        return True

    def default(self, inp):

        if inp == '1':
            return self.do_hadoop(inp)
        elif inp == '2':
            return self.do_spark(inp)
        elif inp == '3':
            return self.do_jupyter(inp)
        elif inp == '4':
            return self.do_sonar(inp)
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        else:
            return self.do_unrecognised(inp)

    do_EOF = do_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()