def respond(msg):
    msg = msg.lower()

    if "balance" in msg:
        return "You can check your balance on the dashboard."
    if "withdraw" in msg:
        return "Go to Withdraw section and select amount."
    if "fraud" in msg:
        return "Fraud is detected when transactions are unusual."
    return "Sorry, I only assist with ATM related queries."
