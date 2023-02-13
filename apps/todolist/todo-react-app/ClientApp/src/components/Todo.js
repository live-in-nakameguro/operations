// Todoコンポーネント
export const Todo = () => {
    return (
      <div>
        <h1>Todoリスト</h1>
        <input type="text" />
        <button>追加</button>
        <ul>
            <li>
              <input type="checkbox" />
              <span>プログラミング</span>
              <button>削除</button>
            </li>
            <li>
              <input type="checkbox" />
              <span>ランニング</span>
              <button>削除</button>
            </li>
        </ul>
      </div>
    );
  };
