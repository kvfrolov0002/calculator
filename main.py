from flask import Flask, request, abort
import calculator

app = Flask(__name__)

calculator = calculator.Calculator()

@app.route('/', methods=['POST'])
def post_example():
    try:
        data = request.get_json()
        problem = data.get('problem')
        if not problem:
            raise ValueError("Необходим ввод выражения в параметр problem")

        result = calc.evaluate(problem)
        return {"result": result}
    except ValueError as ve:
        abort(400, str(ve))
    except Exception as e:
        abort(500, str(e))

if __name__ == '__main__':
    app.run()
