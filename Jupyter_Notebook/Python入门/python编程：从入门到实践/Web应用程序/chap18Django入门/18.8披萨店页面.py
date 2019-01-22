"""
1. 先定义路由
path('pizzas', views.pizzas, name='pizzas'),
path('pizza/<int:pizza_id>', views.pizza, name='pizza'),

2. 编写视图
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    topping = topic.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'topping': topping}
    return render(request, 'pizzas/pizza.html', context)

3. 编写模板
pizzas.html
{% extends "pizzas/base.html" %}
{% block content %}
  <p>Pizzas</p>
  <ul>
  {% for pizza in pizzas %}
    <li><a href="{% url 'pizza' pizza.id %}">{{ pizza }}</a></li>
    {% empty %}
      <li>No pizzas have been added yet.</li>
  {% endfor %}
  </ul>
{% endblock content %}

pizza.html
{% extends "pizzas/base.html" %}
{% block content %}
  <p>Pizzas : {{ pizza }}</p>
  <ul>
  {% for t in topping %}
    <li>
      <p>{{ t.date_added|date:'M d, Y H:i' }}</p>
      <p>{{ t.name }}</p>
    </li>
    {% empty %}
      <li>There are no topping for this topic yet.</li>
  {% endfor %}
  </ul>
{% endblock content %}
"""