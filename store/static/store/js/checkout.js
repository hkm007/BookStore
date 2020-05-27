const quantity = (id)=>{
    qtyHtml = document.getElementById('qty')
    tot = document.getElementById('tot')
    qty = qtyHtml.value

    if(id == 'minus')
    {
        if(qty == 1)
        {
            tot.value = parseFloat(localStorage.getItem("price")).toFixed(2)

        }
        else{
            qty = parseInt(qty)
            qty-=1
            qtyHtml.value = qty
            tot.value = parseFloat(qty* localStorage.getItem("price")).toFixed(2)
        }
    }
    else if ('plus')
    {
        qty = parseInt(qty)
        qty+=1
        qtyHtml.value = qty
        tot.value = parseFloat(qty* localStorage.getItem("price")).toFixed(2)
    }
    
}

const checkPage = document.getElementById('checkoutPage')

if(checkPage != null)
{
    const qty = document.getElementById('qty')
    const price = document.getElementById('bookPrice')
    const tot = document.getElementById('tot')

    localStorage.setItem("price",parseFloat(price.innerHTML))
    tot.value = parseFloat(price.innerHTML).toFixed(2)
    qty.value = 1
}










