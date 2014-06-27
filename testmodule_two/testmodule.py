from osv import fields,osv,orm



class testmodule(orm.Model):
    
    _inherit='testmodule'
    _columns={
      'testmodule_two':fields.char('Test Module Two',size=64),
    }
