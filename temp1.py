from django.db.models import Q

from main.models import Realty

query = "дома закрытая территория "  # Поисковый запрос

# Разбиваем поисковый запрос на отдельные слова
search_terms = query.split()

# Создаем объект Q для каждого слова и объединяем их с использованием оператора Q.OR
q_objects = Q()
for term in search_terms:
    q_objects |= Q(info__iregex=term)

# Выполняем поиск с использованием созданного объекта Q
queryset = Realty.objects.filter(Q(info__iregex=q_objects) | Q(title__iregex=q_objects))


print(search_terms)
print('****')
print(queryset)