


//这是reducer
const reducer = (state, action) => {
    if(!state) return{
        visibility:{}
    } 
    

    switch (action.type) {
        case 'SetInvisible':
            state.visibility = action.visibility
            return {...state,visibility:state.visibility};
        default:
            return state;
    }
}
export default reducer