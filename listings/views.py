from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(ModelViewSet):
    """
    API endpoint for managing listings.
    Provides: GET, POST, PUT, PATCH, DELETE
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(ModelViewSet):
    """
    API endpoint for managing bookings.
    Provides: GET, POST, PUT, PATCH, DELETE
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
