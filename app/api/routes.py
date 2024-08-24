from flask import Blueprint, request
from deepface.commons.logger import Logger
from app.services import services

logger = Logger()
blueprint = Blueprint("routes", __name__)


@blueprint.route("/verify", methods=["POST"])
def verify():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img1_path = input_args.get("img1") or input_args.get("img1_path")
    img2_path = input_args.get("img2") or input_args.get("img2_path")

    if img1_path is None:
        return {"message": "you must pass img1_path input"}

    if img2_path is None:
        return {"message": "you must pass img2_path input"}

    verification = services.verify(
        img1_path=img1_path,
        img2_path=img2_path,
        model_name=input_args.get("model_name", "VGG-Face"),
        detector_backend=input_args.get("detector_backend", "opencv"),
        distance_metric=input_args.get("distance_metric", "cosine"),
        align=input_args.get("align", True),
        enforce_detection=input_args.get("enforce_detection", True),
        anti_spoofing=input_args.get("anti_spoofing", False),
    )

    logger.debug(verification)

    return verification
