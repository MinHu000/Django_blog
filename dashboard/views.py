from django.shortcuts import render
from datetime import datetime

def dashboard_view(request):
    # 🔹 더미 데이터 (나중에 Edge 값으로 교체)
    context = {
        "current_count": 23,
        "status": "정상",
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render(request, "dashboard/dashboard.html", context)
