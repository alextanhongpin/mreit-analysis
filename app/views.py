from flask import request, render_template, url_for, Response
import wikipedia
from app.models import *

def initViews (app):
  @app.route('/', methods=['GET', 'POST'])
  def index():
    if request.method == 'GET':
      return 'Index Page'
    else:
      return 'At POST Route'

  @app.route('/date/<date>')
  def show_date_page(date):
    sort_by = 'date' if request.args.get('sort_by') == None else request.args.get('sort_by')
    reits = select_reits_by_date(date, sort_by)
    def getKey(custom):
      return custom[sort_by]
    return render_template('date.html', reits=sorted(reits, key=getKey))

  @app.route('/reits/<name>')
  def reit(name):
    sort_by = 'date' if request.args.get('sort_by') == None else request.args.get('sort_by')
    reits = select_reit_by_name(name, sort_by)
    keyword = wikipedia.search(name)
    print(keyword)
    if (len(keyword)):
      summary = wikipedia.summary(keyword[0])
    else:
      summary = 'No summary available'
    def getKey(custom):
      return custom[sort_by]
    return render_template('index.html', reits=sorted(reits, key=getKey), summary=summary)

  @app.route('/reits')
  def reits():
    reits = select_reits()
    return render_template('reits.html', reits=reits)

  # @app.route('/csv/<name>')
  # def csv_route(name):
  #   reits = select_reit_to_csv(name)
  #   csv_data = []
  #   for reit in reits:
  #     row = ', '.join(reits[reit])
  #     csv_data.append(row)
  #   csv_string = '\n'.join(csv_data)
  #   return Response(csv_string, mimetype="text/csv", headers={"Content-disposition":"attachment; filename=" + name + ".csv"})