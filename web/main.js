

window.addEventListener('beforeunload', function (e) {
    e.preventDefault();
    e.returnValue = '';
});

window.onload = function() {
    var form = document.querySelector("form");
    form.onsubmit = submitted.bind(form);
}
//alert("runnnig the js...")


function submitted(event) {
    event.preventDefault();
    str = window.location.href;
    if (str.substr(str.length - 10) == 'index.html') {
        addTag();
    }
    else {
        search();
    }
}
//window.addEventListener("close", test);
function test() {
    //eel.PythonCheck();
    alert("Got here");
}

function changeMeme(x) {
    var Image = document.getElementById("theImage");
    Image.src = x;
    //Image.style.class = 'img1';
    var memeTitle = document.getElementById("theMeme");
    memeTitle.innerText = 'meme: '+x;
    //Image.appendChild(img)
    var box = document.getElementById("tagsBox");
    box.innerHTML = '';
}
eel.expose(changeMeme);

function addTag() {
    var tag = document.getElementById("theTag");
    //alert(tag);
    eel.addTagBackend(tag.value);
    tag.value = '';
}

function addTagFrontend(x) {
    var box = document.getElementById("tagsBox");
    var tag = document.getElementById("blankTag");
    var tag2 = tag.cloneNode(true);
    //alert(tag2.children[1].innerText);
    tag2.children[1].innerText = x;
    tag2.style.display = "";
    box.appendChild(tag2);
    //eel.addTagBackend(tag.value);
    //tag.value = '';
}
eel.expose(addTagFrontend);


function deleteTagFrontend() {
    var parent = event.target.parentNode;
    eel.deleteTagBackend(parent.children[1].innerText);
    parent.remove();
    //alert("Yaay!");
}


function addTagTEST(x) {
    var tag = document.getElementById("testTag");
    //var tagBox = document.getElementById("tagsBox");
    var tag2 = tag.cloneNode(true);
    var i;
    for (i=0;i<x;i++) {
        y = i;
        tag2 = tag.cloneNode(true);
        tag2.children[1].innerText = y.toString();
        document.getElementById("tagsBox").appendChild(tag2);
    }   
}

//function JSCheck() {
//    alert("Got here");
//    eel.PythonCheck();
//}
//eel.expose(JSCheck);

function changeToIndex() {
    //window.location.replace("index.html");
    eel.PythonCheck();
    window.location = "index.html";
}

function changeToSearch() {
    //window.location.replace("index.html");
    eel.PythonCheck();
    window.location = "search.html";
}

function search() {
    tags = document.getElementById("theTags").value;
    var body = document.body;
    //alert(body.children.length);
    while (body.children.length != 4) {
        //body.children[body.length-1].remove();
        body.lastChild.remove();
    }
    eel.searchPython(tags);
}

function addTagFrontend2(x) {
    //msg = "now going to add tag "+x;
    //alert(msg);
    var body = document.body;
    var meme = body.children[body.children.length-2];
    var box = meme.children[2];
    //alert(box.id);
    var tag = document.getElementById("blankTag");
    var tag2 = tag.cloneNode(true);
    //alert(tag2.children[1].innerText);
    tag2.children[1].innerText = x;
    tag2.style.display = "";
    box.appendChild(tag2);
    //eel.addTagBackend(tag.value);
    //tag.value = '';
}

function addMeme(x) {
    //alert(x);
    var body = document.body;
    var meme = document.getElementById("blankMeme");
    var meme2 = meme.cloneNode(true);
    meme2.children[0].src = x[0];
    meme2.children[1].innerText = 'meme' + x[0];
    //alert(x.length);
    meme2.style.display = "inline-block";
    //meme2.style.display
    body.appendChild(meme2);
    var br = document.createElement("BR");
    body.appendChild(br);
    var i;
    for (i=1;i<x.length;i++) {
        //msg = 'This meme has '+x.length+' tags.'
        //alert(msg);
        addTagFrontend2(x[i]);
    }
    //alert(typeof(x));
    //alert(typeof(x));
    //alert(x[2]);
}
eel.expose(addMeme);



//function f() {
//        var box = document.getElementById("theBox");
//        //box.innerHTML = eel.f1();
//        eel.f1(box.innerText);
//}