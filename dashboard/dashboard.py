import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)


# Layout интерфейса
app.layout = html.Div([
    html.H1("Прогноз ЛГО и количества клиентов"),
    html.Label("ID пользователя"),
    dcc.Input(id="user_id", type="number", value=1),
    html.Label("Текущая квалификация"),
    dcc.Input(id="prev_qual", type="number", value=0),
    html.Label("Текущий ЛГО"),
    dcc.Input(id="prev_lgo", type="number", value=0),
    html.Label("Месяц"),
    dcc.Input(id="month", type="number", value=1),
    html.Label("Год"),
    dcc.Input(id="year", type="number", value=2023),
    html.Button('Получить прогноз', id='button'),
    html.H3("Прогноз ЛГО:"),
    html.Div(id="lgo_prediction"),
    html.H3("Прогноз клиентов:"),
    html.Div(id="clients_prediction"),
])


# Callback функция для обработки нажатия кнопки
@app.callback(
    [Output("lgo_prediction", "children"), Output("clients_prediction", "children")],
    [Input("button", "n_clicks")],
    [
        Input("user_id", "value"),
        Input("prev_qual", "value"),
        Input("prev_lgo", "value"),
        Input("month", "value"),
        Input("year", "value"),
    ],
)
def update_output(n_clicks, user_id, prev_qual, prev_lgo, month, year):
    # Запрос к FastAPI для получения прогноза
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "user_id": user_id,
            "prev_qual": prev_qual,
            "prev_lgo": prev_lgo,
            "month": month,
            "quarter": (month - 1) // 3 + 1,
            "year": year,
        },
    )
    data = response.json()
    lgo_prediction = data["lgo_prediction"]
    clients_prediction = data["clients_prediction"]
    return str(lgo_prediction), str(clients_prediction)


# Запуск приложения
if __name__ == "__main__":
    app.run_server(debug=True)
