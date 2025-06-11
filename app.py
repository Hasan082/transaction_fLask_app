# Import libraries
from flask import Flask, jsonify, render_template, request, redirect, url_for
# Instantiate Flask functionality
app = Flask("TransactionApp")
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/', methods=['GET'])
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':        
        id = len(transactions) + 1
        date = request.form.get('date')
        amount = request.form.get('amount', 0, type=int)
        transactions.append(
            {'id': id, 'date': date, 'amount': amount}
        )
        return redirect(url_for('get_transactions'))
    else:
        return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = next((trans for trans in transactions if trans['id'] == transaction_id), None)
    if not transaction:
        return "Transaction not found", 404
    if request.method == 'GET':
        return render_template('edit.html', transaction=transaction)
    # Handle POST request to update the transaction
    if request.method == 'POST':
        transaction['date'] = request.form.get('date', transaction['date'])
        transaction['amount'] = int(request.form.get('amount', transaction['amount']))
    return redirect(url_for('get_transactions'))
            
# Delete operation
@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    global transactions
    transactions = [trans for trans in transactions if trans['id'] != transaction_id]
    return redirect(url_for('get_transactions'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)