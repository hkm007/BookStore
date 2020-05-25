const quantity = (id)=>{
    qtyHtml = document.getElementById('qty')
    const price = document.getElementById('bookPrice') 
    qty = qtyHtml.innerHTML
    if(id == 'minus')
    {
        if(qty == 1)
        {
            price.innerHTML = parseFloat(localStorage.getItem("price")).toFixed(2)
        }
        else{
            qty = parseInt(qty)
            qty-=1
            qtyHtml.innerHTML = qty
            console.log(qty)
            console.log(localStorage.getItem("price"))
            price.innerHTML = parseFloat(qty* localStorage.getItem("price")).toFixed(2)
        }
    }
    else if ('plus')
    {
        qty = parseInt(qty)
        qty+=1
        qtyHtml.innerHTML = qty
        console.log(qty)
        console.log(price.innerHTML)
        price.innerHTML = parseFloat(qty* localStorage.getItem("price")).toFixed(2)
    }
    
}

const checkPage = document.getElementById('checkoutPage')

if(checkPage != null)
{
    const price = document.getElementById('bookPrice')
    localStorage.setItem("price",parseFloat(price.innerHTML))
}










