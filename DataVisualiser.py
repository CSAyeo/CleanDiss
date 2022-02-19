from matplotlib import pyplot as plt


def PlotCurrentData(RealData, PredictedData):
    plt.plot(RealData, color = 'red', label = 'Actual Portfolio Guardrail')
    plt.plot(PredictedData, color = 'blue', label = 'Predicted Guardrail')
    plt.title('Portfolio Preditions')
    plt.xlabel('Time')
    plt.ylabel('Portfolio Guardrail')
    plt.legend()
    plt.show()
