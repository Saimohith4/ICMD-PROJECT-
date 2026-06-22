import boto3
from django.shortcuts import render

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1'
)

metrics_table = dynamodb.Table('MetricsTable')
alerts_table = dynamodb.Table('AlertsTable')


def home(request):

    metrics = metrics_table.scan().get('Items', [])
    alerts = alerts_table.scan().get('Items', [])

    metrics = sorted(
        metrics,
        key=lambda x: x.get('timestamp', ''),
        reverse=True
    )

    alerts = sorted(
        alerts,
        key=lambda x: x.get('timestamp', ''),
        reverse=True
    )

    latest_cpu = 0

    if metrics:
        latest_cpu = float(metrics[0].get('cpu', 0))

    cpu_labels = [
        item.get('timestamp', '')
        for item in metrics[:10]
    ]

    cpu_values = [
        float(item.get('cpu', 0))
        for item in metrics[:10]
    ]

    context = {
        'latest_cpu': latest_cpu,
        'metrics': metrics[:10],
        'alerts': alerts[:10],
        'cpu_labels': cpu_labels,
        'cpu_values': cpu_values,
    }

    return render(
        request,
        'dashboard/home.html',
        context
    )