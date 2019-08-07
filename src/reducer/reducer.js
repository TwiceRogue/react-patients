


//这是reducer
const reducer = (state, action) => {
    if(!state) return{
        visibility:{}
    } 
    

    switch (action.type) {
        case 'setInvisible':
            return {columnName:action.columnName, visibility:false};
        default:
            return state;
    }
}
export default reducer