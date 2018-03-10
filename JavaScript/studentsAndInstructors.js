var students = [ 
    {first_name : 'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
];

var users = {
    'Students': [ 
        {first_name : 'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
        ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
        ]
    };

function objectStuff(obj) {
    for(var list in obj) {
        // console.log(obj[list]);
        console.log(obj[list].first_name + " " + obj[list].last_name);
    }
}
objectStuff(students);

// Extra stuff

function moreStuff(obj) {
    for(var bigCategory in obj) { // bigCat is each bigger 'key' inside the entire obj thing
        console.log(bigCategory);

        var newObj = obj[bigCategory]; // newObj is whatever each key is containing.

        // if(obj.hasOwnProperty(bigCategory)) {
        //     for(list in newObj) {
        //         // console.log(obj[bigCategory.list].first_name)
        //         console.log((list+1) + " - " + newObj[list].first_name + " " + newObj[list].last_name + " - " + newObj[list].first_name.length + newObj[list].last_name.length);
        //     }
        // }
        // console.log(newObj)

        for(var i = 0; i < newObj.length; i++){
            console.log((i+1) + " - " + newObj[i]["first_name"] + " " + newObj[i]["last_name"] + " - " + (newObj[i]["first_name"].length + newObj[i]["last_name"].length));
        }

        // for(list in newObj) {
        //     // console.log(obj[bigCategory.list].first_name)
        //     console.log((list+1) + " - " + newObj[list].first_name + " " + newObj[list].last_name + " - " + newObj[list].first_name.length + newObj[list].last_name.length);
        // }
    }
}

moreStuff(users);
// console.log(users['Students']);
