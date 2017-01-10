import unittest
import todo_repo

class TestTodoRepo(unittest.TestCase):

    def test_createTodo(self):
        todo = todo_repo.createTodo("todo")
        self.assertEqual(todo.name, "todo")

    def test_saveTodo(self):
        todo = todo_repo.createTodo("todo")
        todo_repo.saveTodo(todo)
        

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
#    def test_add(self):
#        self.assertEqual(add(1,5), 6)

if __name__ == '__main__':
    unittest.main()