from osv import fields,osv,orm

class testmodule(orm.Model):
    
    _name='testmodule'
    _columns={
      'name':fields.char('Name',size=64),
      'input_a':fields.integer('Input A'),
      'input_b':fields.integer('Input B'),
      'result':fields.integer('Result'),
    }

    def on_change_number(self, cr, uid, ids, input_a,input_b,context):
        value = {}
        print context
        if input_a or input_b:
            value['result'] = input_a + input_b
        return {'value' : value } 