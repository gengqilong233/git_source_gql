from xml.parsers.expat import ParserCreate
import string

class DefaultSaxHandle():
    def start_element(self, name, attrs):
        self.name = name
        print('start_element:%s, attrs:%s' % (name, attrs))

    def end_element(self, name):
        print('end_element:%s' % name)


    def char_data(self, text):
        if text.strip():
            print('%s text is %s' %(self.name, text))

handler = DefaultSaxHandle()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element # <book>
parser.EndElementHandler = handler.end_element # </book>
parser.CharacterDataHandler = handler.char_data # <title>character dataa</title>

with open(r'D:\pycharm\PythonImport\RealLearn\python_bug\learn_new\xpath\book', 'r') as f:
    parser.Parse(f.read())