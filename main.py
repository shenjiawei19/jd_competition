from action.action_first import action_first
from action.action_second import action_second
from action.action_third import action_third
from action.action_fourth import action_fourth
from action.action_sixth import action_sixth
from action.action_predict_first import action_predict_first
from action.action_predict_third import action_predict_third
from train.train_first import train_first
from train.vialid import vialid
# a = action_first('JData_Action_201602.csv')
# print (a)
# print (action_second())
# print (action_third('2016-02-02','2016-02-16'))
# print (action_fourth())
# print (action_sixth())
# print (action_predict_first('JData_Action_201604.csv', '2016-04-06', '2016-04-10'))
# print (action_predict_third())
# print (train_first('JData_Action_201604.csv','2016-04-11','2016-04-15'))
vialid('predict_result-2.csv', 'train_result.csv')
