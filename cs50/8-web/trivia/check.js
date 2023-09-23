// Ensures the webpage is fully loaded before running the functions; DOM: Document Object Model; A DOM element refers to any object in the DOM tree, including HTML tags.
// Event arg is not needed to be passed to the function as the EventListener is tring to detect whether the webpage is fully loaded.
document.addEventListener('DOMContentLoaded', function(){
/*
querySelector is a JS method that selects and return the first element(NULL if not found) that matches a specific CSS selector; CSS selectors include and not limited to:
1. Type selectors, which match elements based on their tag name
2. Class selectors, which match elements based on their class attribute
3. ID selectors, which match elements based on their 'id' attribute
NOTE: querySelectorAll can be use to select and return all of the element inside an array.
*/
    // Type selector; adding a eventlistener to the selected tag.
    document.querySelector('section').addEventListener('click', function(event){
        // Function by convention takes in the arg: event; browser creates an event object that contains information about the event, in this case a click of the mouse;
        // The event.target property is a reference to the element that triggered the event, in this case: button.
        if(event.target.id === 'mcq1')
        {
            mcq1.style.backgroundColor = 'Green';
            mcq1.textContent = 'Correct!';
        }
        else if(event.target.id === 'mcq2')
        {
            mcq2.style.backgroundColor = 'Red';
            mcq2.textContent = 'Incorrect!';
        }
        else if(event.target.id === 'mcq3')
        {
            mcq3.style.backgroundColor = 'Red';
            mcq3.textContent = 'Incorrect!';
        }
    })

    document.querySelector('form').addEventListener('submit', function(event){
        // ID selector; accessing it's value.
        let ans = document.querySelector('#ans').value;
        ans = ans.toLowerCase();
        // By default everytime a form is submitted, the page will reload and data is passed to the server. preventDefault() can prevent this from happening.
        event.preventDefault();
        if (ans === 'hyper text markup language')
        {
            document.querySelector('#freeresponse').style.backgroundColor = 'Green';
            document.querySelector('#freeresponse').textContent = 'Correct!';
        }
        else
        {
            document.querySelector('#freeresponse').style.backgroundColor = 'Red';
            document.querySelector('#freeresponse').textContent = 'Incorrect!';
        }
    })
})