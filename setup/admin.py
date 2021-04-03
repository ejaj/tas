from django.contrib import admin
from .models import Agent, Customer, AgentUser
from .forms import AgentForm, CustomerForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Register your models here.

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    '''
    Register Agent Model to Admin Panel
    '''
    prepopulated_fields = {'slug': ('name',), }
    list_display = ['name', 'email', 'mobile', 'country', 'status']
    list_filter = ['status']
    search_fields = ['name', 'email', 'mobile']
    exclude = ('created', 'updated')
    actions = ['make_enabled', 'make_disabled']
    form = AgentForm

    def make_enabled(self, request, queryset):
        '''
        Enable marked agents
        :param request:
        :param queryset:
        :return:
        '''
        queryset.update(status=True)

    make_enabled.short_description = "Mark selected agents as enabled"

    def make_disabled(self, request, queryset):
        '''
        Disable marked agents
        :param request:
        :param queryset:
        :return:
        '''
        queryset.update(status=False)

    make_disabled.short_description = "Mark selected agents as disabled"

    def save_model(self, request, obj, form, change):
        '''
        Save a :model:`agents` to database
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        '''
        if not change:
            if not obj.created_id:
                obj.created_id = request.user.id
            if not obj.updated_id:
                obj.updated_id = request.user.id
            obj.save()
            agent_id = Agent.objects.latest('id')
            name = request.POST.get("name")
            user_name = request.POST.get("name").replace(' ', '-')
            name = list(name.split(" "))
            fname = name[0]
            lname = name[-1]

            password = make_password(fname.lower())
            email = request.POST.get("email")

            user = User(
                password=password,
                username=user_name.lower(),
                first_name=fname,
                last_name=lname,
                email=email
            )
            user.save()
            user_id = User.objects.latest('id')
            agent_user = AgentUser(
                user=user_id,
                agent=agent_id,
                plain_password=fname.lower()
            )
            agent_user.save()


        else:
            obj.updated_id = request.user.id
            obj.save()


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['agent', 'customer_name', 'passport_number', 'passport_expire_date', 'visa_number',
                    'visa_expire_date', 'amount', 'status']
    list_filter = ['status']
    search_fields = ['agent', 'customer_name', 'passport_number', 'passport_expire_date', 'visa_number',
                     'visa_expire_date', 'status', 'amount']
    exclude = ('created', 'updated')
    form = CustomerForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                kwargs["queryset"] = Agent.objects.all()
            else:
                try:
                    agent_user = AgentUser.objects.get(user=request.user.id)
                    kwargs["queryset"] = Agent.objects.filter(id=agent_user.agent_id)
                except ObjectDoesNotExist:
                    kwargs["queryset"] = Agent.objects.all()
        else:
            kwargs["queryset"] = Agent.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        '''
        Save a :model:`customer` to database
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        '''
        if not change:
            if not obj.created_id:
                obj.created_id = request.user.id
            if not obj.updated_id:
                obj.updated_id = request.user.id
                # obj.save()

        else:
            obj.updated_id = request.user.id
            # obj.save()
        super().save_model(request, obj, form, change)
