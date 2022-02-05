var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        var qty = document.getElementById('qty-' + productId).value;
        console.log('qty: ', qty)
        console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser') {
            addCookieItem(productId, action, qty)
        } else {
            updateUserOrder(productId, action, qty)
        }
    })
}

function updateUserOrder(productId, action, qty) {
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action, 'quantity': qty})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            location.reload()
        });
}

function addCookieItem(productId, action, qty) {
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity': qty}

        } else {
            cart[productId]['quantity'] += 1
            // cart[productId]['quantity'] = qty
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload()
}