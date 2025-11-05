from rest_framework import viewsets, permissions, generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Activity
from .serializers import UserSerializer, ActivitySerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework import permissions, status


# 🧩 Register new users
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# 👤 User management (for admin or testing)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# 💪 Activity management (requires login)
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show the logged-in user’s activities
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically link new activity to the logged-in user
        serializer.save(user=self.request.user)


# 🚪 Logout (blacklist refresh token)
class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]  # 👈 Allow anyone to call logout

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token is None:
                return Response({"detail": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except (TokenError, InvalidToken):
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
