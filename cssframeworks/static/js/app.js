class JsonForm {
    constructor(elem, data) {
        this.data = data;
    }
    display() {
        console.log(this.data)
    }
}

// class Dog extends Animal {
//     constructor(name) {
//         super(name); // スーパークラスのコンストラクターを呼び出し、name パラメータを渡す
//     }

//     speak() {
//         console.log(`${this.name} barks.`);
//     }
// }
