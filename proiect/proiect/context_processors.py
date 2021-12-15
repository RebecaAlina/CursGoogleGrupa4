from aplicatie2.models import Pontaj


def is_ready_to_work(request):
    if request.user.is_authenticated:
        # filter => poate sa returneze unul sau mai multe obiecte
        #        => daca nu gaseste niciun oiect, nu apare eorare
        # get    => returneaza un singur obiect
        #        => daca nu gaseste niciun obiect sau returneaza mai multe obiecte returneaza eroare
        if Pontaj.objects.filter(user_id=request.user.id, end_date=None).exists():
            return {'ready_to_work': False}
        return {'ready_to_work': True}
    return {}
