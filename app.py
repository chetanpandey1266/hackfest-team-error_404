
from flask import Flask, render_template, request
import os, subprocess
from PIL import Image
import shutil

app = Flask(__name__)

app.config["STYLE_IMAGE"] = "STYLE_IMAGE"
app.config["TARGET_IMAGE"] = "TARGET_IMAGE"
app.config["ALLOWED_IMG_EXTENSION"] = ["jpg", "png", "jpeg"]
app.config["MAKEUP_MODEL"] = "MAKEUP_MODEL"
app.config["MAKEUP_OUTPUT"] = "MAKEUP_OUTPUT"
app.config["FASHION_INPUT"] = os.path.join(os.getcwd(), "FashionPlus/datasets/images/")
app.config["FASHION_OUTPUT"] = os.path.join(os.getcwd(), "FashionPlus/classification/data_dict/shape_and_feature/results/demo/images/")
app.config["SIZE_PREDICTION_MODEL"] = "SIZE_PREDICTION_MODEL"
app.config["SIZE_PREDICTION_OUTPUT"] = "SIZE_PREDICTION_OUTPUT"

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/services', methods=["POST", "GET"])
def services():
	if request.method=="GET":
		return render_template('services.html', predicted="False")
	else:
		print(request.files, request.form)
		if request.files:
			style = request.files["style"]
			target = request.files["target"]
			style_fname, style_ext = style.filename.split(".");
			if style_ext in app.config["ALLOWED_IMG_EXTENSION"]:
				select = request.form["options"]
				if (select == "makeup"):
					target_fname, target_ext = target.filename.split(".");
					# makeup script
					print('makeup')
				elif (select == "fashion"):
					style.save(os.path.join("./static/fashion_in", f"{style_fname}.{style_ext}"))
					os.chdir("./FashionPlus")
					# print(os.getcwd())
					style.save(os.path.join(app.config["FASHION_INPUT"], f"{style_fname}.{style_ext}"))
					subprocess.call(f"bash ./fashionp.sh {style_fname}.{style_ext}", shell=True)
					os.chdir("..")
					print(os.getcwd())
					print('fashion')
					shutil.copyfile(os.path.join(app.config["FASHION_OUTPUT"], f"reconstructed_{style_fname}.{style_ext}"), os.path.join(os.getcwd(), f"static/fashion_op/reconstructed_{style_fname}.{style_ext}"))
				return render_template("services.html",predicted=True, style_out=f"fashion_op/reconstructed_{style_fname}.{style_ext}", style_in=f"fashion_in/{style_fname}.{style_ext}")

		return render_template('services.html')

@app.route('/contact')
def contact():
	return render_template('contact-us.html')


@app.route('/<link>')
def notfound(link):
	return render_template('404.html')


app.run(debug=True)
