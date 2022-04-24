function createFormControl(tagname, labelname, name, value, options){
    let div = document.createElement("div");
    if (options.css_framework==="uikit"){
        div.classList.add("uk-form-control","uk-margin");
    }
    console.log(options);
    if (options.crud==="create" && (options.default==="auto_increment"||options.default==="serial")){
        div.classList.add("uk-form-control","uk-hidden");
    }
    if (tagname=="input"){
        let label_div = document.createElement("div");
        let label = document.createElement("label");
        label.innerText = labelname;
        label_div.appendChild(label);
        let input_div = document.createElement("div");
        let input = document.createElement(tagname);
        if (options && options.type){
            input.type = options.type;
            if (options.css_framework==="uikit"){
                input.classList.add(`uk-${options.type}`);
            }
        } else {
            input.type = "text";
            if (options.css_framework==="uikit"){
                input.classList.add("uk-input");
            }
        }
        input.id = name;
        input.name = name;
        input.value = value;
        if (options.index == "pk"){
            console.log("options.index == 'pk'", options.index=="pk");
            input.readOnly = true;           // not readonly
        }
        input_div.appendChild(input);
        div.appendChild(label_div);
        div.appendChild(input_div);
    }
    return div;
}

/**
 * data: json data required
 * options
 *   css_framework: "uikit",
 *   crud: "create",  
 *   // or update, delete
 *   columns
 *   { 
 *     fieldname: 
 *     {
 *       title: field label,
 *       primary_key: true or false,
 *   }
*/
function createForm(crud, row, columns, options){
    let form_elem = document.createElement("form");
    form_elem.classList.add("form");
    Object.keys(row).forEach(function(key){
        let form_options = {
            crud : crud,
            css_framework : options.css_framework,
        }
        const column = JSON.parse(JSON.stringify(columns[key]));
        const label_text = column.label?column.label:key;
        if (column.index){
            form_options.index = column.index;
        }
        if (column.default){
            form_options.default =column.default;
        }
        let div = createFormControl("input", label_text, key, row[key], form_options);
        form_elem.appendChild(div);
    });
    return form_elem;
}
