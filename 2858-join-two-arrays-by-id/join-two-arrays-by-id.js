/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let result = []
    const map = {}

    for (const a1 of arr1){
        map[a1.id] = a1
    }

    for (const a2 of arr2){
        if(map[a2.id]){
            map[a2.id] = {...map[a2.id], ...a2}
        } else {
            map[a2.id] = a2
        }
    }

    return Object.values(map).sort((a, b) => a.id - b.id)
};