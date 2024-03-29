from flask_restful import reqparse

parserAdd = reqparse.RequestParser()
parserAdd.add_argument('name', required=True)
parserAdd.add_argument('about', required=True)

parserAddWord = reqparse.RequestParser()
parserAddWord.add_argument("author", required=True)
parserAddWord.add_argument("hieroglyph", required=True)
parserAddWord.add_argument("translation", required=True)
parserAddWord.add_argument("transcription", required=True)
parserAddWord.add_argument("phrase_ch", required=True)
parserAddWord.add_argument("phrase_ru", required=True)
parserAddWord.add_argument("image", required=True)
parserAddWord.add_argument("front_side_audio", required=True)
parserAddWord.add_argument("left_side_audio", required=True)
parserAddWord.add_argument("right_side_audio", required=True)
parserAddWord.add_argument("up_side_audio", required=True)
parserAddWord.add_argument("down_side_audio", required=True)
