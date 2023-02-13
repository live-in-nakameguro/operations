import React from 'react';

const initToDoList = [
    {
      id: 1,
      name: "教える",
      isComplete: false,
    },
    {
      id: 2,
      name: "ベースを作る",
      isComplete: true,
    },
];
  
export class Todo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            toDoList: initToDoList
        };
    }

    changeToDoStatus = id => {
        let changeToDoList = [];
        this.state.toDoList.map((todo) => {
            if(todo.id == id){
                todo.isComplete = !todo.isComplete;
            }
            changeToDoList.push(todo);
        })
        this.setState({toDoList: changeToDoList});
    }

    showToDoList = () => {
        return (
            this.state.toDoList.map((todo) => (
                <li key={todo.id}>
                    <input 
                        type="checkbox"
                        onClick={() => this.changeToDoStatus(todo.id)}
                        checked={todo.isComplete}
                    />
                    {todo.isComplete ? (
                        <span style={{ textDecorationLine: "line-through" }}>
                            {todo.name}
                        </span>
                        ) : (
                        <span>
                            {todo.name}
                        </span>
                    )}
                    <button>
                        delete
                    </button>
                </li>
              ))
        );
    }

    render() {
        return (
            <div>
                <h1>Todo List</h1>
                <div>
                    <input type="text" />
                    <button>
                        Add
                    </button>
                </div>
                {this.showToDoList()}
            </div>
        );
    }
}
