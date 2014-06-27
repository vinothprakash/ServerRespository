from osv import fields,osv,orm



class testmodule(orm.Model):
    
    _inherit='testmodule'
    _columns={
      'testmodule_one':fields.char('Test Module One',size=64),
    }
