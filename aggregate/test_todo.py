import unittest
from .todo import Todo

class TestTodo(unittest.TestCase):
  
    def test_updateName(self):
        todo = Todo('name')
        self.assertEqual(todo.name, 'name')
        
        todo.updateName('test')
        self.assertEqual(todo.name, 'test')
        

if __name__ == '__main__':
    unittest.main()