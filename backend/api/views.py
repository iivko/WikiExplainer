from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Explanation
from .output_parser import SummaryText
from .serializers import ExplanationSerializer
from .wiki_explainer import explainer


class ExplanationView(APIView):
    def get(self, request):
        explanations = Explanation.objects.all()

        if not explanations.exists():
            return Response(
                data={"msg": "There are no created AI explanations."},
                status=status.HTTP_404_NOT_FOUND
            )

        explanations_serialized = ExplanationSerializer(explanations, many=True)

        response_data = {
            "msg": explanations_serialized.data
        }

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        explanation_serializer = ExplanationSerializer(data=request.data)

        print(explanation_serializer)
        print()

        if not explanation_serializer.is_valid():
            print(explanation_serializer.data)

            topic = explanation_serializer.data["topic"]

            # text here is of type SummaryText (Pydantic object)
            summary, image_url = explainer(topic=topic)

            print(topic)
            print()
            print(summary.text)
            print()
            print(summary.facts)
            print(image_url)

            explanation = Explanation.objects.create(
                topic=topic,
                text=summary.to_dict(),  # Store as JSON
                image_url=image_url
            )

            serialized_explanation = ExplanationSerializer(explanation)

            return Response(
                data=serialized_explanation.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=explanation_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )